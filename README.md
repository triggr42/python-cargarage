# Car Management Application

## Overview
Car Management Application is a console-based tool designed to streamline the management of cars for a small car rental company operating from a single outlet in the UK. With this application, users can efficiently track the status of each car, whether it's on loan or parked in the garage. Key functionalities include managing the car registry, adding or removing cars, and saving registry updates to a file for future reference.

## CarRegistry.dat File
The CarRegistry.dat file serves as the database for the application, storing crucial details about each car, such as ID, registration plate, manufacturer, model type, etc. The data is organized in a comma-separated format, making it easy to read and update.

## UI Functionality
The user interface offers a seamless experience, providing intuitive functionalities to manage car operations effectively:

### Displaying Car Registry
Upon launching the application, users are presented with a comprehensive list of cars from the Car Registry file, along with a menu offering various functional options.

### Adding Cars to Registry
Users can effortlessly add new cars to the registry by entering relevant details such as registration number, manufacturer, model/type, SIPP code, etc.

### Removing Cars from Registry
Removing cars from the registry is a straightforward process, requiring users to specify the position number of the car they wish to remove.

### Managing Car Status
The application allows users to mark cars as hired out or returned to the garage, ensuring accurate tracking of each car's status.

### Updating Car Registry
Changes made to the car registry are promptly saved to the CarRegistry.dat file, ensuring data integrity and consistency.

### Exiting Application
Users can exit the application with a simple confirmation prompt, providing a seamless end-user experience.

## Usage
1. Clone or download the application from the repository.
2. Ensure the CarRegistry.dat file is available in the specified location.
3. Open Main.py in the IDE of choice and run. Ensure all files are in the same location.
4. Follow the on-screen instructions to navigate through various functionalities, such as adding, removing, or updating cars in the registry.

## Classes
The application is structured into four classes, each serving a specific purpose:

### 1. Program
Contains the Main() method responsible for initiating the application.

### 2. UI
Manages the user interface, facilitating smooth interaction and processing user inputs effectively.

### 3. CarRegistry
Handles the management of the car registry, including adding, removing, and updating cars as per user commands.

### 4. Car
Represents a car object with essential properties and validation rules, ensuring accurate data representation and integrity.

## Additional Functionality
The application goes beyond basic functionalities to offer enhanced features, including:
1. Ability to return to the main menu during car addition process for user convenience.
2. Custom Exception classes for robust error handling and enhanced user experience.
3. Protective logic to prevent exceptions, ensuring smooth application execution.
4. Static UI without scrolling, providing a consistent and clutter-free interface.
5. File integrity checks to ensure data consistency and reliability, enhancing overall application robustness.

## Conclusion
Car Management Application is a powerful tool designed to streamline car management operations for small rental companies. With its intuitive interface and robust functionalities, it offers a seamless user experience while ensuring accurate tracking and management of car inventory.
