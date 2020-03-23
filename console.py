
from argparse import ArgumentParser
import os
import downloader
_COMMAND_DOWNLOAD = 'download'


def _add_parser_category_download(subparsers):
    parser = subparsers.add_parser(
        _COMMAND_DOWNLOAD, help='downloads the file from the URL.')
    parser.set_defaults(command=_COMMAND_DOWNLOAD)

    parser.add_argument(
        'url',
        type=str,
        help='input url to be downloaded.')

    parser.add_argument(
        '-mp3',
        '--convert-to-mp3',
        action='store_true',
        help='whether the url should be converted to mp3.')


def _parse_arguments():
    parser = ArgumentParser(description='Console interface for the parser.')
    parser.set_defaults(command=None)

    subparsers = parser.add_subparsers(help='Category')
    _add_parser_category_download(subparsers)
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()

    elif args.command == _COMMAND_DOWNLOAD:
        file_path = downloader.download_youtube_video(args.url)
        if args.mp3:
            downloader.convert_video_to_mp3(file_path)

    else:
        print("Invalid Command")

    return (args.command, args)


def main():
    (command, args) = _parse_arguments()


if __name__ == "__main__":
    main()
