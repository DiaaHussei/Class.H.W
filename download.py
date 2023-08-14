'''
 WebScrapping implies getting something from the web..
'''


#To download a video using URL in Python, we  use the requests library. Here's an example code:

import requests

url = "https://example.com/video.mp4"
filename = "video.mp4"

response = requests.get(url)

with open(filename, "wb") as f:
    f.write(response.content)
    print("Video downloaded successfully!")


'''
In this code, we first define the URL of the video and the filename that we want to save it as. 
We then use the requests.get() method to get the content of the URL. 
We open a file with the specified filename in binary write mode and write the content of the response to it.'''

#Finally, we print a success message.