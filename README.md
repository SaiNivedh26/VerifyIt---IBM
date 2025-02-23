# VerifyIt - Verify Truth in an Instant 
<h3>Part of IBM-Granite Hackathon 2025 ⚡ </h3>
<div>
  <img 
    src="https://github.com/user-attachments/assets/c9719f5d-99f3-489e-9285-dba22da2c526" 
    alt="VerifyIt Logo" 
    style="height: 600px; width: 600px; float: left;"
  >



</div>

---

## **About VerifyIt**
VerifyIt: The ultimate, lightweight, and high-speed fact-checking Chrome extension designed to empower your digital journey. Whether you're navigating news, social media, or research, VerifyIt lets you instantly check the authenticity of any content, all without interrupting your reading experience.

At the core of VerifyIt lies advanced web scraping technology, which seamlessly gathers data from multiple sources across the web. This enables it to analyze and cross-check information in real time, ensuring reliable and accurate fact verification.

With its distraction-free UI, VerifyIt integrates effortlessly into your browsing, providing integrity checks for facts without compromising your focus. Experience fast, efficient fact-checking and stay informed without missing a beat!

### Key Innovative Features

- **Real-Time Verification**: **Scrapes Web data** to validate any statement instantly.  
- **Clean, Minimalist Interface** : Simple, clean, and intuitive extension design built based on User preference
- **Comprehensive Analysis**: Ranks sources by credibility and provides a Trust scores, source credibility, detailed analysis 
- **Privacy-First Approach**: Ensures your queries remain private and secure. And comes with access to history of all recent fact checks, for instant recap
- **Multilingual Article Analysis** : For Supported languages by Granite model. this Includes English, German, Spanish, French, Japanese, Portuguese, Arabic, Czech, Italian, Korean, Dutch, Chinese (Simplified)

---
### Building Steps ⚡
## **Google Specific Framework used**

- **Custom Search API**
- **Programmable Search Engine by Google**
- **granite3.1-moe** ( long-context mixture of experts (MoE) Granite models from IBM designed for low latency usage. )
  
## **Frontend**
- HTML5 & Bootstrap CSS: Responsive, modern design
- JavaScript: Dynamic, interactive user experience

## **Backend**
- Flask API: Robust server-side processing and to handle asynchronous requests
- Google Custom Search API: Comprehensive information retrieval
- Crawl4AI: Intelligent web scraping framework
- Granite : Advanced content truthfulness evaluation, with Customized prompt template
- Chrome's Local Storage: To ensure the history of the user's VerifyIt searches are stored and are accessible

### 🔧 Unique Technical Innovations

- **Adaptive Search Query Generation**: Dynamically creates contextual search queries
- **Intelligent Content Analysis**: Uses AI to understand nuanced information contexts
- **Secure, Lightweight Extension**: Minimal performance overhead
  
---

## Pipeline
![Target Input is taken by the backend](https://github.com/user-attachments/assets/7c6a9703-9d60-45ac-b853-47c6c05a6bf9)

---

---

## 🧩 **How It Works**
1. Clone the repo and follow the **Installation Instructions**.
2. Highlight any statement or click on the Analysis Button.
3. Let VerifyIt scrape, analyze, and rank the results.
4. Get instant feedback with a truthfulness score and credible sources.

---

## 💡 **Installation Instructions**
1. Clone this repository:  
   ```bash
   git clone https://github.com/thespectacular314/VerifyIt-ChromeExtension.git
   ```

2. Navigate to the extension directory:  
   ```bash
   cd VerifyIt-ChromeExtension
   ```

3. Create a `.env` file for API keys:  
   - In the root of your project directory, create a file named `.env`.
   - Add the following content to your `.env` file, replacing `your_key` with the actual values:
     ```env
     SEARCH_ID="your_search_id"
     CUSTOM_API="your_custom_api_key"
     ```
   - Ensure `.env` is added to `.gitignore` to keep your keys private:
     ```bash
     echo ".env" >> .gitignore
     git add .gitignore
     git commit -m "Add .env to .gitignore"
     ```

4. Load the extension:
   - Open Chrome.
   - Go to `chrome://extensions`.
   - Enable **Developer Mode**.
   - Click on **Load unpacked** and select the project folder.

5. Install all the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
     
6. Start the backend server:
   ```bash
   python3 app.py
   ```

7. Use the extension:
   - Go to any webpage you want to fact-check and click the **Analysis button** at the bottom left for a complete URL analysis.
   - Alternatively, select text and **right-click** to analyze it.

---

**VerifyIt** - Empowering you to navigate the digital world with confidence and truth.  
