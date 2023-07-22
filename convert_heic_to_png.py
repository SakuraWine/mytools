import argparse
import pathlib
import pillow_heif
from PIL import Image


# コマンドライン引数で対象ディレクトリを受ける
parser = argparse.ArgumentParser(description="convert all heif to png.")
parser.add_argument("-d", "--directory", help="directory")
args = parser.parse_args()


def convert_heic_to_png(directory: str) -> None:
    """指定したディレクトリ内の.heicを.pngへ変換する

    Args:
        directory (str): ディレクトリ
    """
    path = pathlib.Path(directory)
    heic_paths = path.glob("*.heic")
    for heic_path in heic_paths:
        heic = pillow_heif.read_heif(heic_path)
        filename = str(heic_path).replace(".heic", ".png")
        image = Image.frombytes(heic.mode, heic.size,
                                heic.data, "raw", heic.mode, heic.stride)
        image.save(filename, "PNG")


convert_heic_to_png(args.directory)
