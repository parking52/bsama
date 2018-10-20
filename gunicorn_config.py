import multiprocessing

# The recommended initial value is 2*N+1, and should be ~4..16.
workers = multiprocessing.cpu_count() * 2 + 1

worker_class = 'gevent'
worker_connections = 1000

# Log to stdout for Docker & Scalyr.
accesslog = '-'
access_log_format = "%(h)s %(l)s %({connexion.uid}e)s %(t)s \"%(r)s\" %(s)s %(b)s %(L)s %({connexion.client_id}e)s"
