import os
import shutil
import unittest
from glob import glob

from datasets.HomusDatasetDownloader import HomusDatasetDownloader
from datasets.HomusImageGenerator import HomusImageGenerator


class HomusImageGeneratorTest(unittest.TestCase):

    def test_download_extract_and_draw_bitmaps(self):
        # Arrange
        datasetDownloader = HomusDatasetDownloader("temp/raw")

        # Act
        datasetDownloader.download_and_extract_dataset()
        HomusImageGenerator.create_images("temp/raw", "temp/img")
        all_image_files = [y for x in os.walk("temp/img") for y in glob(os.path.join(x[0], '*.png'))]
        actual_number_of_files = len(all_image_files)

        # Assert
        self.assertEqual(15200, actual_number_of_files)

        # Cleanup
        os.remove("HOMUS-2.0.zip")
        shutil.rmtree("temp")


if __name__ == '__main__':
    unittest.main()