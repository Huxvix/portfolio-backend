from cloudinary_storage.storage import RawMediaCloudinaryStorage

class CloudinaryPDFStorage(RawMediaCloudinaryStorage):
    #  optional defaults
    options = {"resource_type": "raw"}