import datetime

class Scheduler:
    @staticmethod
    def compute_charge_slots(solar, prices, batteries, night_start, night_end):
        # Combine solar & price forecasts into a score: prefer high solar, low price
        slots = []
        for s in solar:
            time = datetime.datetime.fromisoformat(s["time"][:-1])
            price = next((p["price"] for p in prices if p["time"] == s["time"]), None)
            score = s["irradiance"] - (price or 0) / 10
            slots.append((time, score))
        slots.sort(key=lambda x: x[1], reverse=True)
        return slots  # Top slots to charge
