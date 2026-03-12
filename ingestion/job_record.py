from dataclasses import dataclass, field
from typing import Any


def _require_non_empty_string(data: dict[str, Any], field_name: str) -> str:
    value = data.get(field_name)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Job record field '{field_name}' must be a non-empty string.")
    return value.strip()


def _optional_string(data: dict[str, Any], field_name: str) -> str | None:
    value = data.get(field_name)
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError(f"Job record field '{field_name}' must be a string when provided.")

    normalized = value.strip()
    return normalized or None


def _normalize_tags(value: Any) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValueError("Job record field 'tags' must be a list of strings when provided.")

    normalized_tags: list[str] = []
    for tag in value:
        if not isinstance(tag, str) or not tag.strip():
            raise ValueError("Each tag must be a non-empty string.")
        normalized_tags.append(tag.strip())
    return normalized_tags


@dataclass(slots=True)
class JobRecord:
    job_id: str
    title: str
    company: str
    location: str
    description: str
    url: str | None = None
    source: str | None = None
    posted_at: str | None = None
    salary: str | None = None
    tags: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "JobRecord":
        if not isinstance(data, dict):
            raise ValueError("Each job record must be a dictionary.")

        return cls(
            job_id=_require_non_empty_string(data, "job_id"),
            title=_require_non_empty_string(data, "title"),
            company=_require_non_empty_string(data, "company"),
            location=_require_non_empty_string(data, "location"),
            description=_require_non_empty_string(data, "description"),
            url=_optional_string(data, "url"),
            source=_optional_string(data, "source"),
            posted_at=_optional_string(data, "posted_at"),
            salary=_optional_string(data, "salary"),
            tags=_normalize_tags(data.get("tags")),
        )

    def text_for_embedding(self) -> str:
        return "\n".join(
            [
                f"Title: {self.title}",
                f"Company: {self.company}",
                f"Location: {self.location}",
                f"Description: {self.description}",
            ]
        )

    def metadata(self) -> dict[str, Any]:
        return {
            "job_id": self.job_id,
            "title": self.title,
            "company": self.company,
            "location": self.location,
            "url": self.url,
            "source": self.source,
            "posted_at": self.posted_at,
            "salary": self.salary,
            "tags": self.tags,
        }


def load_job_records(raw_jobs: list[dict[str, Any]]) -> list[JobRecord]:
    if not isinstance(raw_jobs, list):
        raise ValueError("The jobs payload must be a list of job records.")

    return [JobRecord.from_dict(raw_job) for raw_job in raw_jobs]
