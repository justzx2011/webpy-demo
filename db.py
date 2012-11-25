import config
def listing(**k):
    return config.DB.select('user', **k)