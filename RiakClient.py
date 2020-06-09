import riak


class RiakClient:

    def __init__(self, host, port):
        self.client = riak.RiakClient(host=host, port=port)

    def get_bucket(self, name='s21808'):
        return self.client.bucket(name)

    def add_object(self, data, key=None):
        bucket = self.get_bucket()
        obj = bucket.new(key, data={**data})
        obj.store()

    def get_object(self, key):
        bucket = self.get_bucket()
        obj = bucket.get(key)
        return obj

    def update_object(self, key, new_data):
        obj = self.get_object(key)
        for k, v in new_data.items():
            obj.data[k] = v
        obj.store()

    def delete_object(self, key):
        obj = self.get_object(key)
        obj.delete()



