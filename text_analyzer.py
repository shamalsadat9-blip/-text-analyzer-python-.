import re
from collections import Counter

def analyze_text(text):
    # حساب عدد الحروف الكلي
    total_chars = len(text)
    
    # استخراج الكلمات واستثناء الفواصل والرموز
    words = re.findall(r'\b\w+\b', text.lower())
    total_words = len(words)
    
    # حساب عدد الجمل تقريبياً
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]
    total_sentences = len(sentences)
    
    # حساب الوقت المقدر للقراءة (بمعدل 200 كلمة في الدقيقة)
    read_time = round(total_words / 200, 2)
    
    # معرفة الأكثر 3 كلمات تكراراً
    word_counts = Counter(words)
    most_common = word_counts.most_common(3)
    
    # عرض النتائج
    print("\n" + "="*30)
    print("📊 نتائج تحليل النص:")
    print("="*30)
    print(f"📝 عدد الكلمات: {total_words}")
    print(f"🔤 عدد الحروف: {total_chars}")
    print(f"📑 عدد الجمل: {total_sentences}")
    print(f"⏱️ وقت القراءة المتوقع: {read_time} دقيقة")
    
    print("\n🌟 الكلمات الأكثر تكراراً:")
    for word, count in most_common:
        print(f" - '{word}': {count} مرة")
    print("="*30)

# تجربة البرنامج
if __name__ == "__main__":
    user_input = input("أدخلي النص الذي تريدين تحليله:\n")
    if user_input.strip():
        analyze_text(user_input)
    else:
        print("⚠️ لم تدخلي أي نص!")

