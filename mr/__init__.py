# coding = utf-8


class Reader(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def create_readers(cls, config):
        raise NotImplementedError


class Job(object):
    def __init__(self, reader):
        self.reader = reader
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_jobs(cls, reader_class, config):
        jobs = []
        for reader in reader_class.create_readers(config):
            jobs.append(cls(reader))
        return jobs


class Runner:
    def __init__(self, job_class, reader_class, config):
        self.jobs = job_class.create_jobs(reader_class, config)

    def run(self):
        # map phase
        for job in self.jobs:
            job.map()

        # reduce phase
        first_job, other_jobs = self.jobs[0], self.jobs[1:]
        for other_job in other_jobs:
            first_job.reduce(other_job)
        return first_job.result
