# spark-local-setup
**Repo with ready-to-run Spark jobs or notebooks.**

This setup lets you run PySpark notebooks/jobs directly inside VS Code, connected to the Spark cluster. You get an isolated environment without needing to manually install Python, PySpark, or Jupyter locally.

## Prerequisites

Make sure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)
- [VS Code](https://code.visualstudio.com/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) (optional, for VS Code)

---

## Project Structure

```
project-root/
├── .devcontainer/
│   └── devcontainer.json
├── docker-compose.yml
├── requirements.txt
├── jobs/
│   └── example_job.py
└── notebooks/
    └── example_notebook.ipynb
```

- `jobs/` — Python scripts using PySpark  
- `notebooks/` — Jupyter notebooks  
- `requirements.txt` — Python dependencies (shared for all jobs and notebooks)

---

## Option 1: Using VS Code Dev Containers

1. **Open the project in VS Code**

    ```bash
    code .
    ```

    Reopen in Dev Container:

    Press `fn + F1` → search “Dev Containers: Rebuild and Reopen in Container”.

    VS Code will build the container based on `docker-compose.yml` and `devcontainer.json`.

2. **Run PySpark jobs**

    ```bash
    python /home/jovyan/jobs/example_job.py
    ```

3. **Run notebooks**

    - Open any `.ipynb` file in `notebooks/`.
    - The pre-configured kernel has PySpark ready — run cells directly.
    - Spark UI logs are accessible in VS Code output and web UI.

---

## Option 2: Using Docker Compose Directly

1. **Build and start containers**

    ```bash
    docker-compose up -d
    ```

    This will start:
    - Spark master + Spark history server
    - Jupyter notebook/lab
    - Mounts for jobs, notebooks, and logs

2. **Access Jupyter Lab**

    - Open your browser: [http://localhost:8888](http://localhost:8888)
    - Use the token specified in `docker-compose.yml` (e.g., `yourtoken123`).

3. **Run PySpark scripts inside the container**

    ```bash
    docker exec -it pyspark bash
    python /home/jovyan/jobs/example_job.py
    ```

4. **Spark UI**

    - Spark Master UI: [http://localhost:8080](http://localhost:8080)
    - Spark Application UI: [http://localhost:4040](http://localhost:4040)
    - History Server: [http://localhost:18080](http://localhost:18080)

---

## Adding Dependencies

Edit `requirements.txt` with any packages you need, e.g.:

```
pandas
numpy
matplotlib
findspark
```

- **If using Dev Container:**

    Press `fn + F1` → search “Dev Containers: Rebuild and Reopen in Container”

- **If using Docker Compose directly:**

    ```bash
    docker exec -it jupyter pip install -r /home/jovyan/requirements.txt
    ```