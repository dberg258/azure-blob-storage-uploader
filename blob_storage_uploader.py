from azure.storage.blob import BlockBlobService
import os

storage_key = "<storage_key>"
storage_account_name = "<storage_account_name>"
storage_container_name = "<container_name>"
block_blob_service = BlockBlobService(account_name=storage_account_name, account_key=storage_key)

files = []

while True:
    path_to_folder = input("Enter path to folder containing files: ")
    if os.path.exists(path_to_folder):
        break
    else:
        print("File path does not exist.")

for r, d, f in os.walk(path_to_folder):
    for file in f:
        files.append(os.path.join(r, file))

blobs = block_blob_service.list_blobs(storage_container_name)
blobs = [blob.name for blob in blobs]

print("Uploaded Documents:")
counter = 0
for file_path in files:
    file_name = file_path.rsplit('\\', 1)[-1]
    if file_name in blobs:
        continue
    block_blob_service.create_blob_from_path(storage_container_name, str(file_name), file_path)
    counter += 1
    print(file_name)

print()
print("Number of documents uploaded: " + str(counter))