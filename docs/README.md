---
layout: home
permalink: index.html

# Please update this with your repository name and title
repository-name: e18-4yp-Personalized-Multimodal-Emotion-Prediction
title: Personalized Multimodal Emotion Prediction
---

[comment]: # "This is the standard layout for the project, but you can clean this and use your own template"

# Personalized Multimodal Emotion Prediction

#### Team

- e18354, Ruchira Tharaka, [email](mailto:e18354@eng.pdn.ac.lk)
- e18318, Piyumali Sandunika, [email](mailto:e18318@eng.pdn.ac.lk)
- e18022, Didula Induwara, [email](mailto:e18022@eng.pdn.ac.lk)

#### Supervisors

- Dr. Dharshana Kasthurirathna, [email](mailto:dharshana.k@sliit.lk)
- Ms. Yasodha Vimukthi, [email](mailto:yasodhav@eng.pdn.ac.lk)

#### Table of content

1. [Project Summary](#project-summary)
2. [Publications](#publications)
3. [Links](#links)

---


## Project Summary

Humans express emotions using different modalities like facial expressions, vocal tone and the speech. Each person may express their emotions using different modalities in different proportions. In this research, we introduce a personalized emotion prediction model that focuses on four key emotions: happy, sad, neutral, and angry. What makes this model special is its ability to adapt to each individual user, learning from how they personally express emotions and adjusting the importance of each modality accordingly.

We’ve integrated pretrained models for each modality, and the system gets better over time through feedback from the users. Unlike traditional models that treat everyone the same, this one adapts in real-time, making the emotion detection more accurate and personalized for every user. We used a mechanism based on Online Learning and weighted average ensemble.

### Ensemble model Architecture

![Final_Presentation_Team 8 (3)](https://github.com/user-attachments/assets/923c117d-4d48-4018-8fac-38feb2704da0)

### Experiments & Results

Here’s a quick look at how accurate the model is when it first analyzes the three modalities for different people. The ensemble accuracy shows how well the model performs after it adjusts the weights for each user.

| Person | Text  | Vocal Tone | Image | Ensemble Accuracy |
|--------|-------|------------|-------|-------------------|
| 1      | 0.649 | 0.746      | 0.377 | 0.762             |
| 2      | 0.761 | 0.577      | 0.271 | 0.771             |
| 3      | 0.815 | 0.569      | 0.342 | 0.822             |

As you can see, each person expresses their emotions differently. For example, Person 1 is more expressive with their voice, while Person 2 and 3 rely more on text. But for every situation, our ensembled model gives the highest accuracy of capturing the correct emotion based on its weighted average and iterative learning mechanisms.

![Final_Presentation_Team 8 (2) (1)](https://github.com/user-attachments/assets/cb1d1446-a023-457d-8b12-45200298f04b)


### Limitations and Future Enhancements

One of the main challenges we face is that the datasets used for training might not capture the full range of cultural and age differences. This can lead to biases and affect the model’s ability to generalize in real-world scenarios. Online learning helps the model improve with new data, but issues like data imbalance, privacy concerns, and potential bias still need to be addressed.

Also, since the model is currently trained on English language data, it might struggle with non-native English speakers, especially if their natural speech patterns differ. In the future, we could integrate translation APIs or fine-tune the model with multilingual datasets to make it more accurate for people from diverse linguistic backgrounds.

### Conclusion

In short, this model is a big step forward in personalized emotion detection. By continuously learning from user feedback and adjusting how it weighs different ways people express emotions, it offers more accurate predictions. While there are still challenges to overcome, especially around dataset diversity and multilingual support, this model is well-positioned for applications like mental health monitoring, human-computer interaction, and beyond.

## Publications
[//]: # "Note: Uncomment each once you uploaded the files to the repository"

 1. [Semester 7 report](https://drive.google.com/file/d/1T5Qyu1jfoJ8Vvoy_QXVtqgb5YSCJtaFU/view?usp=sharing)
 2. [Semester 7 slides](https://drive.google.com/file/d/1NHVkD5gQmGyaZUk6nBJBOAoQEg1sDFLX/view?usp=sharing)
 3. [Semester 8 report](https://drive.google.com/file/d/12_NEyqpoYIGLe0sKktD9ir6fudENKj7q/view?usp=sharing)
 4. [Semester 8 slides](https://drive.google.com/file/d/1lSZBhEUSz3cN4NpHtvBicjzTLCQpJtFH/view?usp=sharing)
<!-- 5. Author 1, Author 2 and Author 3 "Research paper title" (2021). [PDF](./). -->


## Links

[//]: # ( NOTE: EDIT THIS LINKS WITH YOUR REPO DETAILS )

- [Project Repository](https://github.com/cepdnaclk/e18-4yp-Personalized-Multimodal-Emotion-Prediction)
- [Project Page](https://cepdnaclk.github.io/e18-4yp-Personalized-Multimodal-Emotion-Prediction/)
- [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)
- [University of Peradeniya](https://eng.pdn.ac.lk/)

[//]: # "Please refer this to learn more about Markdown syntax"
[//]: # "https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet"
