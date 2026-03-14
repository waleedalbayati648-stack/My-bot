import asyncio
from telethon import TelegramClient
from datetime import datetime

# --- بياناتك الشخصية ---
api_id = 35521555
api_hash = 'caa67f765871a5a98e625d9832d4e57b'
phone = '+9647716719536'
target_group = '@syhhb453'

# --- التعديلات الجديدة ---
current_investment = 170000  # المبلغ يبدأ من 170 ألف
speculation_msg = "مضاربه 10000" # إضافة جملة المضاربة

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    global current_investment
    await client.start(phone=phone)
    
    start_time = datetime.now().strftime("%H:%M:%S")
    print(f"[{start_time}] ✅ تم التحديث! البداية من {current_investment}")

    while True:
        try:
            time_now = datetime.now().strftime("%H:%M:%S")
            
            # 1. إرسال: راتب
            await client.send_message(target_group, "راتب")
            print(f"[{time_now}] 🚀 تم إرسال: راتب")
            await asyncio.sleep(2) 

            # 2. إرسال: استثمار + المبلغ
            investment_text = f"استثمار {int(current_investment)}"
            await client.send_message(target_group, investment_text)
            print(f"[{time_now}] 🚀 تم إرسال: {investment_text}")
            await asyncio.sleep(2)

            # 3. إرسال: مضاربه 10000
            await client.send_message(target_group, speculation_msg)
            print(f"[{time_now}] 🚀 تم إرسال: {speculation_msg}")
            await asyncio.sleep(2)

            # 4. إرسال: بخشيش
            await client.send_message(target_group, "بخشيش")
            print(f"[{time_now}] 🚀 تم إرسال: بخشيش")

            # حساب الزيادة 3% للمرة القادمة
            current_investment *= 1.03
            print(f"[{time_now}] 📈 المبلغ القادم سيكون: {int(current_investment)}")
            
        except Exception as e:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ❌ خطأ: {e}")

        # الانتظار لمدة 10 دقائق
        await asyncio.sleep(600)

with client:
    client.loop.run_until_complete(main())
