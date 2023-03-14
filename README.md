# One Mans Trash

"One man's trash is another man's treasure."

One-Mans-Trash is a web application that uses deep learning techniques to detect and classify different types of trash objects in images, such as plastic bottles, cans, cups, and plastic bags. The app also computes an estimated selling price for each detected object based on published selling prices for recyclable materials in the Philippines.

The detection model only detects objects in 10 classes: bottles, bottle caps, cans, cups, lids, plastic bag + wrappers, pop tabs, straws, cigarettes, and others for objects detected not in those categories.

This project served as a milestone for me in learning how to leverage openly available work online and deploying machine learning-powered applications on Google Cloud.

For the deep learning model and data, I made use of the object detection deep learning model, [Mask RCNN](https://github.com/matterport/Mask_RCNN), published by matterport and trained on the [Trash Annotations in Context](http://tacodataset.org/) (TACO) dataset.

## Demo

Click on the link below (ran on Google Cloud Run):

[One-Mans-Trash](https://tinyurl.com/one-mans-trash)

Works on laptops, tablets, and mobile devices!

## Usage/Examples

1. Click the link in the *Demo* section
2. Once the web application has loaded, click the `Browse files` button and upload an image of some trash you have.
[Web app home screen](screenshots/screenshot_1.png)
3. Once the image has been uploaded, click the `Detect Trash` button.
[Uploaded image and detection loading](screenshots/screenshot_2.png)
4. The final output should be an estimate of how much your trash is worth and a processed image of your upload showing what it detected.
[Final output](screenshots/screenshot_3.png)

## Improvements

The goal of the project was to learn how to leverage a deep learning model I've never worked with before, package it into a web application, and deploy it to the cloud. Although I was able to accomplish those goals with this projects, there are a lot of improvements that could be made:

- The detection model's accuracy - the model sometimes detects obscure figures in the background of the image and attempts to classify them. This can be improved by gathering more/better data, training the model for longer, and increasing the prediction confidence threshold.
- Model serving - currently, the model is served directly on the frontend in streamlit which means that users will also have to wait for the model to build and load on top of making the prediction. A future version could use model artifact served on GCP's AI Platform that's called using an api.

## Screenshots
[Detected plastic bottles](screenshots/screenshot_4.png)
[Detected coffee table items](screenshots/screenshot_5.png)

## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
 - https://github.com/pedropro/TACO
 - https://github.com/matterport/Mask_RCNN
 - https://www.philstar.com/entertainment/2012/06/10/815637/cash-trash