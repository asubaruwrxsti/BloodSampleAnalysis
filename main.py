def main():
    try:
        import uvicorn
        uvicorn.run("api.api:app", host="localhost", port=8000, reload=True)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()