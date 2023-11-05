# NewHacks

## Inspiration
Have you ever found yourself struggling to maintain focus and well-being during long work or study sessions? We sure have. The inspiration for ProdWatch stems from our desire to create a supportive and adaptive tool that enhances productivity. 

## What it does

This browser extension tracks your facial expressions and surroundings to keep you motivated, focused, and healthy. By giving you encouraging messages when you're unhappy, telling you to take breaks when you're tired, or reminding you to get back to work when you're distracted, ProdWatch is a dynamic and adaptable tool that is perfect for anyone who wants to up their productivity. 


## How we built it

We trained and deployed a CNN in TensorFlow using a Kaggle dataset to identify facial features and expressions (such as fatigure/tiredness). 
We used an OpenCV pre-trained model for the eye-tracker feature, which would identify whether the user was focused on the screen or was looking elsewhere. 
We used Chrome.Extension API for our front-end, coding it in JavaScript, and we used Flask to connect the program together. 

## Challenges we ran into

Issues included building an accurate CNN that would be able to detect facial expressions and emotions with high accuracy. The dataset we used had many ambiguous cases, for which we had to adapt our model to. 

None of our team members had much experience in front-end development, so we all had to learn the basics of browser extensions and JavaScript. We also did not have any experience in running Python files on the web, so we also had to learn the basics of Flask. Likewise, UI and UX design was a challenge, as none of us had training or much experience in this area as well, even though UI/UX was to be a crucial part of our extension to work effectively. 

Due to the nature of the private video recordings that our extension would manage, it was a challenge to make sure that our private video recordings were secure and not accessible to others (outside of the user). 



## Accomplishments that we're proud of

Self-building and adapting our CNN architecture from about **50% accuracy to 88% accuracy**. 
Hosting the data locally keeps sensitive data (such as recordings of users' activity) private. 


## What we learned

We learned skills in Machine Learning engineering, specifically how to deploy our own convolutional neural network model into an active browser extension. 


## What's next for ProdWatch

More features, including audio recognition (hearing the user speak) and detecting tones, pauses, and other aspects of speech will be added; these patterns can be put together to give tips to the user regarding public speaking, especially in situations such as **virtual interviews or speeches**. 

Another aspect that can be worked on is to aggregate the data of whether the user is focused or not, and the user can view their past history 

