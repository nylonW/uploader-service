# VideoHandler

`VideoHandler` is a Python utility designed to monitor specific directories for new video files and subsequently upload them to YouTube. It leverages the `watchdog` library to observe folder changes and a custom tool, `youtubeuploader`, to handle the YouTube upload process.

## Features

- **Directory Monitoring**: Constantly watches specified folders for new video additions.
- **Automatic Upload**: As soon as a new video is detected, it's uploaded to YouTube.
- **Metadata Management**: Uses associated JSON metadata files to provide video details during the upload.
- **Post-Upload Organization**: After successful upload, videos are moved to an `/uploaded/channel` directory for better organization.

## Setup

1. Ensure the `youtubeuploader` tool is in the same directory as the script or in the system's PATH.
2. Make sure the `client_secrets.json` file for each channel is available in the respective channel directory.
3. Install required Python libraries:
   ```
   pip install watchdog
   ```

## Usage

1. Set the base folder path in the main script:
   ```python
   base_folder = "channels"
   ```

2. Run the script:
   ```
   python main.py
   ```

3. The script will start monitoring the specified `channels` folder and its nested folders for new videos. When a new video is detected, it will be uploaded to YouTube using the provided metadata JSON file.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.