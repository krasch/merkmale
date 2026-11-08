```
export OPEN_API_KEY=YOUR_KEY_GOES_HERE
docker build -t merkmale . 
docker run -e OPENAI_API_KEY=$OPENAI_API_KEY -v ./:/app merkmale
```
