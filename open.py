def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    main()


"""
Traceback (most recent call last):
  File "/tmp/open.py", line 5, in <module>
    main()
  File "/tmp/open.py", line 2, in main
    open("/path/to/mars.jpg")
FileNotFoundError: [Errno 2] No such file or directory: '/path/to/mars.jpg'

The error output makes more sense now. The paths are pointing to a single file called open.py. 
The output mentions that the error starts on line 5, which includes the call to main(). 
Next, the output follows the error to line 2 in the open() function call. 
And finally, FileNotFoundError again reports that the file or the directory doesn't exist.
"""