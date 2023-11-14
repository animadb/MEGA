import mega.py

def save_mega_file_to_mega_account(downloadable_file_url, destination_folder_id):
    """Saves a MEGA file from a downloadable URL to your MEGA account without downloading it to your PC."""

    mega = Mega()
    mega.login("your_mega_email", "your_mega_password")

    file_node = mega.get_file_node_from_downloadable_url(downloadable_file_url)
    mega.move_node(file_node, destination_folder_id)

if __name__ == "__main__":
    downloadable_file_urls = [
        "https://mega.nz/file/d/12345678/90abcdef",
        "https://mega.nz/file/d/98765432/abcdef01",
    ]

    destination_folder_id = "destination_folder_id"

    for downloadable_file_url in downloadable_file_urls:
        save_mega_file_to_mega_account(downloadable_file_url, destination_folder_id)

