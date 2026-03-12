import unittest

from ingestion.job_record import JobRecord, load_job_records


class JobRecordTests(unittest.TestCase):
    def test_from_dict_accepts_valid_record(self):
        job = JobRecord.from_dict(
            {
                "job_id": "job-123",
                "title": "Data Analyst",
                "company": "Nova",
                "location": "Paris",
                "description": "Analyze hiring trends.",
                "url": "https://example.com/job-123",
                "source": "linkedin",
                "posted_at": "2026-03-12",
                "salary": "EUR 45k",
                "tags": ["sql", "python"],
            }
        )

        self.assertEqual(job.title, "Data Analyst")
        self.assertEqual(job.tags, ["sql", "python"])
        self.assertEqual(job.metadata()["source"], "linkedin")

    def test_from_dict_rejects_missing_required_field(self):
        with self.assertRaises(ValueError):
            JobRecord.from_dict(
                {
                    "job_id": "job-123",
                    "title": "Data Analyst",
                    "company": "",
                    "location": "Paris",
                    "description": "Analyze hiring trends.",
                }
            )

    def test_load_job_records_requires_list_payload(self):
        with self.assertRaises(ValueError):
            load_job_records({"job_id": "not-a-list"})

    def test_text_for_embedding_includes_key_fields(self):
        job = JobRecord.from_dict(
            {
                "job_id": "job-123",
                "title": "Data Analyst",
                "company": "Nova",
                "location": "Paris",
                "description": "Analyze hiring trends.",
            }
        )

        text = job.text_for_embedding()

        self.assertIn("Title: Data Analyst", text)
        self.assertIn("Company: Nova", text)
        self.assertIn("Location: Paris", text)


if __name__ == "__main__":
    unittest.main()
