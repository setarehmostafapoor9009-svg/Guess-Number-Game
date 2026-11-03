import random

MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 5

CLOSE_THRESHOLD = 5    # اختلاف تا ۵: خیلی نزدیک
MEDIUM_THRESHOLD = 15  # اختلاف تا ۱۵: متوسط، بیشتر از آن: دور

RANKS = {
    1: "نمونه‌ای!",
    2: "بسیار خوبی",
    3: "خوب",
    4: "قبول",
    5: "با شانس بردی!",
}

# تبدیل ارقام فارسی و عربی به انگلیسی تا کاربر بتواند عدد را فارسی هم بنویسد
DIGIT_MAP = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")


def read_guess():
    """یک حدس معتبر برمی‌گرداند؛ در صورت ورودی نامعتبر None."""
    raw = input("حدست رو وارد کن: ").strip().translate(DIGIT_MAP)
    try:
        guess = int(raw)
    except ValueError:
        print("ورودی نامعتبر است! لطفاً یک عدد صحیح وارد کن. (این تلاش حساب نشد)")
        return None
    if guess < MIN_NUMBER or guess > MAX_NUMBER:
        print(f"عدد باید بین {MIN_NUMBER} تا {MAX_NUMBER} باشد! (این تلاش حساب نشد)")
        return None
    return guess


def closeness_hint(diff):
    if diff <= CLOSE_THRESHOLD:
        return "خیلی نزدیکی!"
    if diff <= MEDIUM_THRESHOLD:
        return "نزدیکی، ولی هنوز فاصله داری!"
    return "خیلی دوری!"


def play_round():
    secret = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempt = 0

    print(f"\nیک عدد بین {MIN_NUMBER} تا {MAX_NUMBER} انتخاب کردم. حدس بزن!")

    while attempt < MAX_ATTEMPTS:
        print(f"\nتلاش {attempt + 1} از {MAX_ATTEMPTS}")
        print(f"جان باقی‌مانده: {MAX_ATTEMPTS - attempt}")

        guess = read_guess()
        if guess is None:
            continue  # ورودی نامعتبر: از فرصت‌ها کم نمی‌شود

        attempt += 1

        if guess == secret:
            print(f"\nآفرین! عدد درست بود: {secret}")
            print(f"تعداد تلاش‌ها: {attempt} | رتبه: {RANKS[attempt]}")
            return

        direction = "کوچک‌تر وارد کن" if guess > secret else "بزرگ‌تر وارد کن"
        print(f"{direction} - {closeness_hint(abs(guess - secret))}")

    print(f"\nباختی! فرصت‌هایت تمام شد. عدد مخفی {secret} بود.")


def ask_play_again():
    while True:
        answer = input("\nدوباره بازی می‌کنی؟ (بله/خیر): ").strip().lower()
        if answer in ("بله", "آره", "y", "yes"):
            return True
        if answer in ("خیر", "نه", "n", "no"):
            return False
        print("لطفاً فقط «بله» یا «خیر» وارد کن.")


def main():
    print("به بازی حدس اعداد خوش آمدی!")
    try:
        while True:
            play_round()
            if not ask_play_again():
                break
    except (EOFError, KeyboardInterrupt):
        print()
    print("خداحافظ!")


if __name__ == "__main__":
    main()
