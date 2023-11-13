import os
import unittest
from urlgennwm import generate_urls  # Import the generate_urls function from your script

class TestGenerateURLs(unittest.TestCase):
    def test_generate_urls_for_medium_range_mem6(self):
        # Define test input values
        start_date = "202201120000"
        end_date = "202201130000"
        fcst_cycle = [0, 8]
        lead_time = [1, 18]
        varinput = 1
        geoinput = 1
        runinput = 2  # Set to 2 for the medium_range_mem6 folder
        urlbaseinput = 2
        meminput = 6

        # Call the function to generate URLs
        generate_urls(start_date, end_date, fcst_cycle, lead_time, varinput, geoinput, runinput, urlbaseinput, meminput)

        # Check if the generated 'filenamelist.txt' file exists
        self.assertTrue(os.path.exists("filenamelist.txt"))

        # Define the expected URLs or patterns for the medium_range_mem6 folder
        expected_urls = [
            "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/post-processed/WMS/nwm.20220112/medium_range_mem6/nwm.t00z.medium_range.channel_rt_6.f001.conus.nc",
            "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/post-processed/WMS/nwm.20220112/medium_range_mem6/nwm.t00z.medium_range.channel_rt_6.f018.conus.nc",
            "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/post-processed/WMS/nwm.20220112/medium_range_mem6/nwm.t08z.medium_range.channel_rt_6.f001.conus.nc",
            "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/post-processed/WMS/nwm.20220112/medium_range_mem6/nwm.t08z.medium_range.channel_rt_6.f018.conus.nc",
            "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/post-processed/WMS/nwm.20220113/medium_range_mem6/nwm.t00z.medium_range.channel_rt_6.f001.conus.nc",
            "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/post-processed/WMS/nwm.20220113/medium_range_mem6/nwm.t00z.medium_range.channel_rt_6.f018.conus.nc",
            "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/post-processed/WMS/nwm.20220113/medium_range_mem6/nwm.t08z.medium_range.channel_rt_6.f001.conus.nc",
            "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/post-processed/WMS/nwm.20220113/medium_range_mem6/nwm.t08z.medium_range.channel_rt_6.f018.conus.nc",
            ]

        # Read the content of the file and check for the expected content
        with open("filenamelist.txt", "r") as file:
            content = file.read()
            for url in expected_urls:
                self.assertIn(url, content)
                
if __name__ == '__main__':
    unittest.main()
