import requests
from dotenv import load_dotenv
import os
from crawl4ai import AsyncWebCrawler
from ollama import chat
from ollama import ChatResponse

load_dotenv()

class GraniteModel:
    def __init__(self):
        self.model_name = "granite3-dense:2b"
        self.generation_config = {
            "temperature": 1,
            "top_p": 0.9,
            "max_tokens": 8192,
            "frequency_penalty": 0.1,
            "presence_penalty": 0.6,
        }

    def generate_search_queries(self, target):
        response: ChatResponse = chat(model=self.model_name, messages=[
            {
                'role': 'user',
                'content': f"Examine the URL and identify the main topic being discussed. Provide the complete main topic on what is being discussed in the url. I dont want any introductory responses from you. {target}",
            },
        ])
        return response['message']['content']
    

    def analyse_url(self, topic, content, target_content=None):
        print("In Analyzing the content")
        
        response: ChatResponse = chat(model=self.model_name, messages=[
            {
                'role': 'user',
                'content': f"[topic: {topic}, Target_content_to_examine: {target_content}, content_to_refer: {content[:2000]}]. "
                        f"Evaluate the accuracy of the title using available web-scraped data. "
                        f"Assign a trust score (0-1) and provide a brief explanation. "
                        f"Format response as a dictionary: {{title, bool, t_score, concl, source}}."
            },
        ], options={"max_tokens": 4096, "temperature": 0.7, "top_p": 0.8})

        print("done by granite")
        return response['message']['content']

    

async def create_crawler(url):
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url=url,
            word_count_threshold=20,
            excluded_tags=['form', 'nav', 'aside', 'footer', 'header', 'iframe', 'script', 'style'],
            remove_overlay_elements=True,
            exclude_external_links=True,
            exclude_social_media_links=True,
        )

        return {url: result.markdown}

def search_urls(search_query=None):
    api_key = os.getenv('CUSTOM_API')
    search_engine_id = os.getenv("SEARCH_ID")

    base_url = "https://www.googleapis.com/customsearch/v1"

    params = {
        'key': api_key,
        'cx': search_engine_id,
        'q': search_query
    }

    response = requests.get(base_url, params=params)
    url = []
    
    if response.status_code == 200:
        response_json = response.json()
        if 'items' in response_json:
            links = response_json['items']
            for item in links:
                print(item['link'])
                url.append(item['link'])
        else:
            print("No 'items' key in response:", response_json)
    else:
        print("Search request failed:", response.status_code, response.text)

    return url