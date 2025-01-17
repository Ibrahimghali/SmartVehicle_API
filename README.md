# Smart Vehicle API

This is a Django-based API project designed for a smart vehicle system. It handles key data points like **vehicle speed**, **location**, **fuel consumption**, and **gas detection**, providing endpoints to manage and interact with this information.

## Features

- **Vehicle Data**: Manage details about vehicles, including their make, model, and unique identifiers.
- **Speed Data**: Track vehicle speed with real-time updates.
- **Location Data**: Monitor vehicle location with GPS data.
- **Fuel Consumption**: Keep track of fuel usage and monitor consumption rates.
- **Gas Detection**: Detect and manage any hazardous gas leaks in the vehicle.

## Project Structure

- `vehicle/`: Contains models, views, and serializers for managing vehicle data.
- `location/`: Handles location-related data, including vehicle GPS coordinates.
- `speed/`: Manages speed data for the vehicles.
- `consumption/`: Tracks fuel consumption data.
- `gas/`: Detects and manages hazardous gas levels in the vehicle.

## Requirements

Before running the project, ensure that you have the following installed:

- Python 3.x
- Django
- SQLite (default database)

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Setup and Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Ibrahimghali/SmartVehicle_API.git
   cd SmartVehicle_API
   ```

2. **Apply database migrations**:

   ```bash
   python manage.py migrate
   ```

3. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

4. The API will be available at `http://127.0.0.1:8000/`.

## Endpoints

### Vehicle Endpoints
- `GET /vehicle/`: List all vehicles.
- `POST /vehicle/`: Create a new vehicle.
- `GET /vehicle/{id}/`: Retrieve details of a specific vehicle.
- `PUT /vehicle/{id}/`: Update vehicle information.
- `DELETE /vehicle/{id}/`: Delete a specific vehicle.

### Location Endpoints
- `GET /location/`: List all locations.
- `POST /location/`: Create a new location entry.
- `GET /location/{id}/`: Retrieve details of a specific location.

### Speed Endpoints
- `GET /speed/`: List all speed data.
- `POST /speed/`: Log new speed data.

### Consumption Endpoints
- `GET /consumption/`: View fuel consumption data.
- `POST /consumption/`: Log fuel consumption data.

### Gas Detection Endpoints
- `GET /gas/`: View gas detection logs.
- `POST /gas/`: Log gas detection data.

## GitHub Repository

You can find the repository on GitHub:

[Smart Vehicle API GitHub](https://github.com/Ibrahimghali/SmartVehicle_API)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.