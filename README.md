# Moments - AI That Makes Image Sharing Smarter  

**Moments** is a Flask-based platform that makes sharing images effortless and intelligent. With the power of **Azure Vision API**, Moments automatically generates alt text for accessibility and searchable tags for better organization. No need to manually tag photos—just upload and let AI do the work.  

## What Makes Moments Special?  

- **AI-Powered Alt Text** – Get instant, accurate descriptions for every image.  
- **Smart Image Tagging** – AI recognizes objects and assigns searchable tags.  
- **Find Images in Seconds** – Use AI-generated tags to search effortlessly.  
- **Customizable Tags** – Edit or add your own tags for more control.  
- **Secure User Accounts** – Log in and manage your profile safely.  
- **Engaging Community Features** – Upload, comment, and connect with others.  

## How AI Describes Your Images  

When you upload a photo, **Azure Vision API** analyzes it and generates a meaningful description. This alt text is stored in the **Photo model** for fast database searches. If you prefer, you can **edit or replace** the AI-generated description before publishing. Every image automatically includes an **alt attribute**, making Moments accessible to all users.  

## Searching Made Easy with AI  

Forget scrolling endlessly to find a picture—Moments makes image search effortless. AI scans each uploaded image, detects objects, and assigns relevant **tags**. These tags are saved in the database so you can quickly find images with a simple keyword search.  

Example: Searching for "sunset" will instantly show all images containing sunsets—without needing to tag them manually.  

## Designed for Simplicity and Control  

- **Alt Text That Works for You** – AI generates descriptions, but you can tweak them.  
- **Search That Just Works** – AI tags every image automatically, making search instant.  
- **No Extra Effort Needed** – Upload an image, and Moments takes care of the rest.  

## Where to Find the Code  

- **GitHub Repository:** [Moments on GitHub](https://github.com/nshrinisha/Hw1-Moments)  
- **Latest Commit:** [View Commit](https://github.com/nshrinisha/Hw1-Moments/commit/main)  

## Get Started in Minutes  

### 1. Clone the Project  
```sh
git clone https://github.com/nshrinisha/Hw1-Moments.git  
cd moments  
```  

### 2. Set Up a Virtual Environment  

For macOS/Linux:  
```sh
python3 -m venv venv  
source venv/bin/activate  
```  

For Windows:  
```sh
python -m venv venv  
venv\Scripts\activate  
```  

### 3. Install Dependencies  
```sh
pip install -r requirements.txt  
```  

## Set Up AI Image Recognition  

Moments relies on **Azure Vision API** to analyze images. Here’s how to connect it:  

1. **Create an Azure Computer Vision account**  
   - Sign up at [Azure Portal](https://portal.azure.com/)  
   - Generate an API Key and Endpoint URL  

2. **Save your credentials securely**  
   - In the root directory, create a `.env` file:  
     ```sh
     AZURE_VISION_API_KEY="your-api-key-here"  
     AZURE_VISION_ENDPOINT="your-endpoint-here"  
     ```  
   - Keep this file private—it should never be pushed to GitHub.  

## Run the App Locally  

To start the Flask server, run:  
```sh
flask run  
```  

Then, open:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)  


## Try Moments Without an Account  

Use this test login to explore:  

- **Email:** admin@helloflask.com  
- **Password:** moments  


Potential Harms & Mitigations
1.	Inaccurate or Misleading Alt Text 
- **Harm:** AI-generated descriptions tend to misinterpret photos, resulting in inaccurate alt text that can be confusing to screen reader-dependent visually impaired users. For example, a dog might be labeled as a wolf, altering its intended meaning.
- **Solution:** To ensure accuracy, let users adjust AI-generated alt text before being published. Additionally, implement confidence thresholds where AI prompts users to verify descriptions if uncertainty is high. Also, a feedback system can enhance predictions for the future.
2.	AI recognition being biased
- **Harm:**  AI models that have been trained on datasets that are not diverse may have trouble recognizing cultural, racial, or regional differences, which could result in the incorrect classification or elimination of items or individuals.
- **Solution:** The way to go is to expand the range of training datasets and include a variety of situations and demographics. Over time, eliminate bias by retraining models based on identified inaccuracies and enabling manual tagging to allow users to fix errors.
3.	AI Processing May Slow Down (Scalability issues)
- **Harm:** When many users upload images at once, Azure Vision API can slow down, causing delays in generating alt text and search results. High traffic might also hit API rate limits, making some images wait in a queue, affecting real-time user experience.
- **Solution:** Cache AI results to avoid unnecessary API calls, making searches faster. Use asynchronous processing to handle uploads in the background, preventing delays. AWS Lambda and other cloud scaling solutions can be used to effectively handle unexpected increases in demand.


## Scaling for the Future  

### Managing Large Volumes of Images  
- **Issue:** Storing thousands of images locally isn’t scalable.  
- **Solution:** Move to cloud storage services like AWS S3.  

### Controlling API Costs  
- **Issue:** Every AI request costs money.  
- **Solution:** Store AI-generated tags in the database to minimize requests.  

### Keeping the App Fast  
- **Issue:** Searching through large databases can slow performance.  
- **Solution:** Use indexing and caching for faster lookups.  
 
