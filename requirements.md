# Requirements

## Problem Statement

Users need a reliable web tool to generate QR codes for common personal, business, and payment data without installing desktop software.

## Objectives

- Generate QR codes instantly.
- Support multiple QR code types.
- Provide preview and PNG download.
- Validate user input.
- Persist generation history locally.

## User Stories

- As a user, I can generate a QR code for a URL.
- As a user, I can download my QR code as a PNG.
- As a user, I can see recent generated QR codes.
- As a user, I receive meaningful validation errors.

## Functional Requirements

- Support text, URL, contact, address, email, phone, SMS, Wi-Fi, UPI, and event QR codes.
- Expose `/generate`, `/download/<id>`, `/history`, and `/health`.
- Store generated images and history.

## Non-Functional Requirements

- Responsive UI.
- Modular Python code.
- Automated tests.
- Docker-compatible runtime.
