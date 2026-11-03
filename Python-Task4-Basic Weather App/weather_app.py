import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from zoneinfo import ZoneInfo

import requests
from PIL import Image, ImageTk
from io import BytesIO

API_KEY = os.getenv("OPENWEATHER_API_KEY", "YOUR_OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"
ICON_URL = "https://openweathermap.org/img/wn/{}@2x.png"


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Now")
        self.root.geometry("760x700")
        self.root.minsize(650, 600)
        self.root.configure(bg="#101827")
        self.unit = "metric"
        self.last_weather = None
        self.last_forecast = None
        self.icon_photo = None

        self.build_ui()

    def build_ui(self):
        title = tk.Label(
            self.root, text="WEATHER NOW", font=("Segoe UI", 23, "bold"),
            bg="#101827", fg="#f8fafc"
        )
        title.pack(pady=(18, 4))

        subtitle = tk.Label(
            self.root, text="Live conditions and a 5-day outlook",
            font=("Segoe UI", 10), bg="#101827", fg="#94a3b8"
        )
        subtitle.pack()

        search_frame = tk.Frame(self.root, bg="#101827")
        search_frame.pack(fill="x", padx=28, pady=18)

        self.city_entry = tk.Entry(
            search_frame, font=("Segoe UI", 12), relief="flat",
            bg="#1e293b", fg="#f8fafc", insertbackground="white"
        )
        self.city_entry.pack(side="left", fill="x", expand=True, ipady=10, padx=(0, 8))
        self.city_entry.insert(0, "Enter city or ZIP (e.g. Kolkata)")

        self.search_btn = tk.Button(
            search_frame, text="Get Weather", command=self.get_weather,
            font=("Segoe UI", 10, "bold"), bg="#38bdf8", fg="#082f49",
            relief="flat", padx=15, pady=9, cursor="hand2"
        )
        self.search_btn.pack(side="left")

        self.location_btn = tk.Button(
            search_frame, text="Use IP Location", command=self.get_ip_location,
            font=("Segoe UI", 9), bg="#334155", fg="#f8fafc",
            relief="flat", padx=10, pady=9, cursor="hand2"
        )
        self.location_btn.pack(side="left", padx=(8, 0))

        self.error_label = tk.Label(
            self.root, text="", font=("Segoe UI", 10), bg="#101827",
            fg="#fca5a5", wraplength=680
        )
        self.error_label.pack()

        self.current_card = tk.Frame(self.root, bg="#1e293b", padx=22, pady=16)
        self.current_card.pack(fill="x", padx=28, pady=8)

        self.city_label = tk.Label(
            self.current_card, text="Search for a location",
            font=("Segoe UI", 17, "bold"), bg="#1e293b", fg="#f8fafc"
        )
        self.city_label.pack()

        self.condition_label = tk.Label(
            self.current_card, text="Weather details will appear here",
            font=("Segoe UI", 11), bg="#1e293b", fg="#cbd5e1"
        )
        self.condition_label.pack(pady=(3, 0))

        self.icon_label = tk.Label(self.current_card, bg="#1e293b")
        self.icon_label.pack()

        self.temp_label = tk.Label(
            self.current_card, text="--°", font=("Segoe UI", 34, "bold"),
            bg="#1e293b", fg="#f8fafc"
        )
        self.temp_label.pack()

        self.details_label = tk.Label(
            self.current_card, text="Humidity: --   |   Wind: --",
            font=("Segoe UI", 11), bg="#1e293b", fg="#cbd5e1"
        )
        self.details_label.pack(pady=(5, 8))

        self.toggle_btn = tk.Button(
            self.current_card, text="Switch to °F", command=self.toggle_units,
            font=("Segoe UI", 9, "bold"), bg="#475569", fg="#f8fafc",
            relief="flat", padx=12, pady=6, cursor="hand2"
        )
        self.toggle_btn.pack()

        forecast_wrap = tk.Frame(self.root, bg="#101827")
        forecast_wrap.pack(fill="both", expand=True, padx=28, pady=(10, 20))

        hourly_title = tk.Label(
            forecast_wrap, text="NEXT 6 HOURS",
            font=("Segoe UI", 11, "bold"), bg="#101827", fg="#7dd3fc"
        )
        hourly_title.pack(anchor="w")

        self.hourly_frame = tk.Frame(forecast_wrap, bg="#101827")
        self.hourly_frame.pack(fill="x", pady=(6, 14))

        daily_title = tk.Label(
            forecast_wrap, text="5-DAY FORECAST",
            font=("Segoe UI", 11, "bold"), bg="#101827", fg="#7dd3fc"
        )
        daily_title.pack(anchor="w")

        self.daily_frame = tk.Frame(forecast_wrap, bg="#101827")
        self.daily_frame.pack(fill="x", pady=(6, 0))

        self.root.bind("<Return>", lambda event: self.get_weather())

    def validate_key(self):
        if not API_KEY or API_KEY == "YOUR_OPENWEATHER_API_KEY":
            self.show_error("Add your OpenWeatherMap API key to the OPENWEATHER_API_KEY environment variable.")
            return False
        return True

    def show_error(self, message):
        self.error_label.config(text=message)

    def get_weather(self):
        location = self.city_entry.get().strip()
        if not location or location == "Enter city or ZIP (e.g. Kolkata)":
            self.show_error("Please enter a city name or ZIP code.")
            return
        if not self.validate_key():
            return

        self.show_error("")
        self.search_btn.config(state="disabled", text="Loading...")
        self.root.update_idletasks()

        try:
            # OpenWeatherMap supports city names and ZIP codes for these endpoints.
            params = {"q": location, "appid": API_KEY, "units": self.unit}
            current = requests.get(f"{BASE_URL}/weather", params=params, timeout=10)
            self.check_response(current)
            weather = current.json()

            forecast = requests.get(f"{BASE_URL}/forecast", params=params, timeout=10)
            self.check_response(forecast)
            forecast_data = forecast.json()

            self.last_weather = weather
            self.last_forecast = forecast_data
            self.render_weather()
        except requests.Timeout:
            self.show_error("The weather service timed out. Please try again.")
        except requests.ConnectionError:
            self.show_error("Network connection failed. Check your internet connection.")
        except requests.RequestException as exc:
            self.show_error(f"Could not retrieve weather data: {exc}")
        except (KeyError, IndexError, ValueError):
            self.show_error("The weather service returned an unexpected response.")
        finally:
            self.search_btn.config(state="normal", text="Get Weather")

    def check_response(self, response):
        if response.status_code == 404:
            raise requests.RequestException("City or ZIP code not found.")
        if response.status_code == 401:
            raise requests.RequestException("Invalid API key. Check your OpenWeatherMap key.")
        if response.status_code == 429:
            raise requests.RequestException("API request limit reached. Please wait and try again.")
        response.raise_for_status()

    def render_weather(self):
        data = self.last_weather
        name = data.get("name", "Unknown")
        country = data.get("sys", {}).get("country", "")
        weather = data["weather"][0]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data.get("wind", {}).get("speed", 0)
        unit_symbol = "°C" if self.unit == "metric" else "°F"
        wind_unit = "m/s" if self.unit == "metric" else "mph"

        self.city_label.config(text=f"{name}, {country}")
        self.condition_label.config(text=weather.get("description", "").title())
        self.temp_label.config(text=f"{round(temp)}{unit_symbol}")
        self.details_label.config(
            text=f"Humidity: {humidity}%   |   Wind: {wind} {wind_unit}"
        )

        icon_code = weather.get("icon")
        if icon_code:
            try:
                image_data = requests.get(ICON_URL.format(icon_code), timeout=8).content
                image = Image.open(BytesIO(image_data)).resize((90, 90))
                self.icon_photo = ImageTk.PhotoImage(image)
                self.icon_label.config(image=self.icon_photo)
            except Exception:
                self.icon_label.config(image="")

        self.render_hourly()
        self.render_daily()

    def render_hourly(self):
        for widget in self.hourly_frame.winfo_children():
            widget.destroy()

        entries = self.last_forecast.get("list", [])[:6]
        for item in entries:
            dt = datetime.fromtimestamp(item["dt"])
            temp = item["main"]["temp"]
            symbol = "°C" if self.unit == "metric" else "°F"
            condition = item["weather"][0]["description"].title()
            card = tk.Frame(self.hourly_frame, bg="#1e293b", padx=8, pady=8)
            card.pack(side="left", fill="x", expand=True, padx=3)
            tk.Label(card, text=dt.strftime("%I %p").lstrip("0"), bg="#1e293b",
                     fg="#94a3b8", font=("Segoe UI", 9)).pack()
            tk.Label(card, text=f"{round(temp)}{symbol}", bg="#1e293b",
                     fg="#f8fafc", font=("Segoe UI", 12, "bold")).pack(pady=4)
            tk.Label(card, text=condition, bg="#1e293b", fg="#cbd5e1",
                     font=("Segoe UI", 8), wraplength=85).pack()

    def render_daily(self):
        for widget in self.daily_frame.winfo_children():
            widget.destroy()

        # The free 5-day forecast is supplied in 3-hour intervals.
        # Select one representative forecast entry per local calendar date.
        by_date = {}
        for item in self.last_forecast.get("list", []):
            date_key = datetime.fromtimestamp(item["dt"]).strftime("%Y-%m-%d")
            if date_key not in by_date:
                by_date[date_key] = item
        entries = list(by_date.values())[:5]

        for item in entries:
            dt = datetime.fromtimestamp(item["dt"])
            temp = item["main"]["temp"]
            symbol = "°C" if self.unit == "metric" else "°F"
            condition = item["weather"][0]["description"].title()
            card = tk.Frame(self.daily_frame, bg="#1e293b", padx=8, pady=8)
            card.pack(side="left", fill="x", expand=True, padx=3)
            tk.Label(card, text=dt.strftime("%a, %d %b"), bg="#1e293b",
                     fg="#94a3b8", font=("Segoe UI", 9)).pack()
            tk.Label(card, text=f"{round(temp)}{symbol}", bg="#1e293b",
                     fg="#f8fafc", font=("Segoe UI", 12, "bold")).pack(pady=4)
            tk.Label(card, text=condition, bg="#1e293b", fg="#cbd5e1",
                     font=("Segoe UI", 8), wraplength=90).pack()

    def toggle_units(self):
        self.unit = "imperial" if self.unit == "metric" else "metric"
        self.toggle_btn.config(text="Switch to °C" if self.unit == "imperial" else "Switch to °F")
        if self.last_weather:
            self.get_weather()


    def get_ip_location(self):
        if not self.validate_key():
            return
        self.show_error("")
        try:
            response = requests.get("https://ipinfo.io/json", timeout=8)
            response.raise_for_status()
            city = response.json().get("city", "")
            if not city:
                self.show_error("Could not detect a city from your IP address.")
                return
            self.city_entry.delete(0, tk.END)
            self.city_entry.insert(0, city)
            self.get_weather()
        except requests.Timeout:
            self.show_error("IP location lookup timed out.")
        except requests.RequestException:
            self.show_error("Could not detect your location. Enter a city manually.")


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
