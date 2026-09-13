```
export OPEN_API_KEY=
docker build -t merkmale . 
docker run -e OPENAI_API_KEY=$OPENAI_API_KEY -v ./:/app merkmale
```