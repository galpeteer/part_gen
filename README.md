# Part Generator API

A FastAPI-based service for generating simplified **FEM-optimized washers and bolts** as STEP files.

The application exposes REST endpoints that accept numerical parameters, generate simplified CAD geometry using **CadQuery**, and return the resulting **STEP file**.

The project also contains a minimal **web UI** for manual interaction.

---

# Project Overview

The goal of this project is:


- CAD model generation with **CadQuery**
- packaging using **uv**
- containerization using **Docker**

also demonstrating: 

- clean separation between **API layer**, **business logic**, and **schemas**
- validation using **Pydantic**
- unit tests for testing the separate layers with **unittest**

---

# Architecture

The the structure of the project is shown below:

```
src/part_generator/
│
├── api/
│   └── schemas.py
│
├── services/
│   └── gen_fastener.py
│
├── templates/
│   └── gui_template.html
│
└── main.py
```

### API layer

- request validation
- endpoint routing
- HTTP responses

### Service layer

- geometry creation
- exporting STEP files

### Schemas

- numeric type validation
- value ranges
- rejection of unexpected input

### Templates

A small HTML frontend allows:

- choosing part type (washer / bolt)
- entering parameters
- triggering generation

---

# Geometry Assumptions

The generated objects has **simplified geometry** suitable for FEM simulation

## Washer

The washer is modeled as a simple **cylindrical ring**, without chamfer or specific shape

Parameters:

| Parameter | Meaning |
|---|---|
| outer_diameter | outside washer diameter |
| inner_diameter | hole diameter |
| thickness | washer thickness |

## Bolt

The bolt is simplified as two cylinders, the head and the shaft

Assumptions about the diameters:


head_diameter  = 1.5 * nominal_diameter
head_thickness = 0.8 * nominal_diameter
shaft diameter is currently the input diameter, however for FEM simulations using the pitch diameter could be considered.


Parameters:

| Parameter | Meaning |
|---|---|
| diameter | nominal bolt diameter |
| length | shaft length |

---

# API Endpoints

## Generate Washer

```
POST v1/generate/washer
```

Example request:

```json
{
  "outer_diameter": 20,
  "inner_diameter": 10,
  "thickness": 5
}
```

Response:

```
washer_{timestamp}.step STEP file download
```

---

## Generate Bolt

```
POST v1/generate/bolt
```

Example request:

```json
{
  "diameter": 10,
  "length": 50
}
```

Response:

```
bolt_{timestep}.step STEP file download
```

---

# Error Handling

Validation errors are handled in two layers.

### Schema validation

Invalid input types or range violations are rejected by Pydantic and return:

```
HTTP 422
```

Examples:

- negative diameter
- missing parameters
- wrong data type
- extra fields

### Domain validation

Logical constraints checked inside the service layer return:

```
HTTP 400
```

Example:

```
inner_diameter >= outer_diameter
```

---

# Installation

The project uses **uv** for dependency management.

Install uv if necessary:

```
https://docs.astral.sh/uv/
```

Then install the project:

```bash
uv sync
```

This installs dependencies and the project itself in editable mode.

---

# Running the API

Start the server with:

```bash
uv run uvicorn part_generator.main:app --reload
```

The API will be available at:

```
http://localhost:8000
```

Interactive documentation:

```
http://localhost:8000/docs
```

---

# Using the Web Interface

Open:

```
http://localhost:8000
```

The UI allows:

1. selecting part type
2. entering parameters
3. generating the STEP model

---

# Running Tests

Run all tests:

```bash
uv run python -m unittest discover -s tests -p "test_*.py"
```

The test suite covers:

- washer geometry
- bolt geometry
- schema validation
- API behavior

---

# Docker

Build the container:

```bash
docker build -t part-generator .
```

Run the container:

```bash
docker run -p 8000:8000 part-generator
```

Then open:

```
http://localhost:8000
```

---

# Known Limitations (requires further inputs)

- Bolt geometry is a simplified representation.
- Washer and bolt dimensions are constrained by upper bounds in the schema for demonstration purposes.
- Generated STEP files are currently written to temporary files on disk.

---

# Possible Improvements

Several improvements could be implemented in a production system.

### File management

File handling methods are determined by the actual team, can be finalized based on further inputs
Currently generated STEP files are written to temporary paths and returned directly.

- automatic cleanup
- dedicated temporary directory
- unique request IDs

### Geometry improvements

- parameterized standards (ISO bolts)
- requirements specific to application

### Frontend improvements

- better parameter validation
- automatic form switching
- preview or parameter presets

### Database

- logging interactions (user, parameters)
- providing parts generated frequently

### Logging

- elaborate logging of script mechanisms for troubleshooting purposes




