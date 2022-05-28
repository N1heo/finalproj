# Batch processing GUI
You are looking at my final project for Ala-Too University, programming language II course. This **app** works with images. More specifically, it can apply filters, add watermarks and change size of them. 

## Description
As I said before, this app process images. For that I used __*pillow*__ library. The *GUI* itself is made using __*tkinter*__ lib. I've decided to use this 2 libs, because I used them before in previous projects and they perfectly match for the batch processing purpose. The app didn't have that much of filters, but it's related to not having enough time. But there is no problems to add any other filter in the future, because the main app anatomy is ready.

The journey wasn't so easy, had to watch a lot of videos and look through lots of websites, but I'm pretty satisfied with the result.

## Idea
Well, when my teacher said to make a GUI with batch processing, the first thing that came to my head is a photo editor. And as I spoke to some of my friends, the same idea was born in their heads too. So, when the theme were chosen, I've decided to just upgrade the previous `pillow` project. 

## Libs
The only lib to download is pillow, you can see the version in `requirements.txt` the rest are built-in.

# GUI

![gui](https://user-images.githubusercontent.com/96371464/170838504-d835f296-e915-43f6-894b-374f8c112c0f.PNG)

Here you can see the appearance of the app. You can search through images right in the GUI. Buttons speak for themselves, but anyway let's just quickly go through them.

## Size

![size](https://user-images.githubusercontent.com/96371464/170839697-2e8e37a1-0e99-4062-a296-244c42a93af7.png)

You can choose size from the list. I made it based on most popular ones.

## FileDialog buttons

![Capture2121](https://user-images.githubusercontent.com/96371464/170839778-62fcc542-c92b-40c1-ad46-058782a083cd.PNG)

When you press one of the 'choose' buttons, the filedialog window opens. There you can choose either watermark or new image to add.
## About section

![ddd](https://user-images.githubusercontent.com/96371464/170839862-8b1c92c6-5445-4f7c-94b0-3d974589c45d.PNG)

## How image look after filter/watermark applied

![Capturedddd](https://user-images.githubusercontent.com/96371464/170839904-737596e2-7221-4e98-a63f-d762174d5c77.PNG)

# About requirements
- Exceptions, classes etc. are used √
- Code linting √
- Logo √
- Mymodudle √
- And the other obvious ones √
</a>

### **Options**
I didn't made them, because my app structure is a bit different from requirements. I suppose there should've been the options, where you choose all the filters and then push the 'batch process' button and it's done. In my case the batch processing is merged with options.

