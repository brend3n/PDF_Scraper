import requests
import 

def main():
    download_file("https://webhome.phy.duke.edu/~rgb/Class/intro_physics_1/intro_physics_1.pdf")

def download_file(download_url):
    response = urllib3.urlopen(download_url)
    file = open("document.pdf", 'wb')
    file.write(response.read())
    file.close()
    print("Completed")

if __name__ == "__main__":
    main()