import streamlit as st
import base64
from PIL import Image, ImageOps

def invert_image_color(image_path):
    # 画像を読み込む
    image = Image.open(image_path)
    # 画像の色を反転させる
    inverted_image = ImageOps.invert(image)
    return inverted_image

# アプリのタイトルを設定
title = "F1ファンのための新通貨 : Bun-Pay "

# カスタムHTMLを使用してタイトルを中央揃えにする
st.markdown(f"<h1 style='text-align: center;'>{title}</h1>", unsafe_allow_html=True)

banner_image = 'bunpay_banner_r1.jpg'

# バナー画像を表示
st.image(banner_image, use_column_width=True)

# ファイルのパスを指定します。
#icons_file = 'icons.jpg'
#st.image(icons_file, use_column_width=True)

balance_html = """
<div style="border: 2px solid #87CEFA; border-radius: 5px; padding: 10px; text-align: center; margin: 20px 0;">
    あなたの残高は<b> 220,000 Bun-pay</b> です。
</div>
"""
st.markdown(balance_html, unsafe_allow_html=True)

# MP3ファイルのパスを指定します。
mp3_file = 'voice-r1.mp3'
mp3_file_kidding = 'kidding.mp3'
mp3_file_tsunoda = 'letsgobaby.mp3'

# カスタムCSSを定義
custom_css = """
<style>
    /* Streamlitボタンのスタイルを変更 */
    .stButton>button {
        font-weight: bold; /* 太文字に設定 */
    }
</style>
"""

# カスタムCSSをページに挿入
st.markdown(custom_css, unsafe_allow_html=True)

# ボタンを作成し、「bun-payで支払う」と表示します。
if st.button('Bun-payで支払う'):
    # ファイルをBase64にエンコード
    audio_file = open(mp3_file, 'rb')
    audio_bytes = audio_file.read()
    base64_audio = base64.b64encode(audio_bytes).decode()

    # カスタムHTMLを作成し、Base64エンコードされたオーディオデータを埋め込む
    audio_html = f"""
    <audio autoplay>
        <source src="data:audio/m4a;base64,{base64_audio}" type="audio/mp3">
    </audio>
    """

    # StreamlitにHTMLを表示
    st.markdown(audio_html, unsafe_allow_html=True)

if st.button('Bun-payでお面を購入する (5% 割引が自動適用されます)'):
    # ファイルをBase64にエンコード
    audio_file = open(mp3_file, 'rb')
    audio_bytes = audio_file.read()
    base64_audio = base64.b64encode(audio_bytes).decode()

    # カスタムHTMLを作成し、Base64エンコードされたオーディオデータを埋め込む
    audio_html = f"""
    <audio autoplay>
        <source src="data:audio/m4a;base64,{base64_audio}" type="audio/mp3">
    </audio>
    """

    # StreamlitにHTMLを表示
    st.markdown(audio_html, unsafe_allow_html=True)


if st.button('Bun-payに全財産をチャージする'):
    # ファイルをBase64にエンコード
    audio_file = open(mp3_file_kidding, 'rb')
    audio_bytes = audio_file.read()
    base64_audio = base64.b64encode(audio_bytes).decode()

    # カスタムHTMLを作成し、Base64エンコードされたオーディオデータを埋め込む
    audio_html = f"""
    <audio autoplay>
        <source src="data:audio/m4a;base64,{base64_audio}" type="audio/mp3">
    </audio>
    """

    # StreamlitにHTMLを表示
    st.markdown(audio_html, unsafe_allow_html=True)

if st.button('Bun-payでDAZNの年会費を支払う / WFTの皆さんにカンパする'):
    # ファイルをBase64にエンコード
    audio_file = open(mp3_file_tsunoda, 'rb')
    audio_bytes = audio_file.read()
    base64_audio = base64.b64encode(audio_bytes).decode()

    # カスタムHTMLを作成し、Base64エンコードされたオーディオデータを埋め込む
    audio_html = f"""
    <audio autoplay>
        <source src="data:audio/m4a;base64,{base64_audio}" type="audio/mp3">
    </audio>
    """

    # StreamlitにHTMLを表示
    st.markdown(audio_html, unsafe_allow_html=True)

legal_notice_html = """
<style>
.legal-notice {
    font-size: 6px; /* 小さな文字サイズ */
    color: gray;
}
</style>
<div class="legal-notice">
    <p>同じボタンを連続で押すと動かない場合があります。また仮想通貨「Bun-pay」の利用に際しては、以下の点にご注意ください：</p>
    <ul>
        <li>利用規約: 「Bun-pay」のレギュレーションを読み、理解した上でご使用ください。</li>
        <li>税務申告: 取引による利益はスチュワードへの申告の対象となる場合があります。</li>
        <li>順位変動: 仮想通貨の順位は大きく変動するため、使用時の順位をご確認ください。</li>
        <li>使用上限: 「Bun-pay」がバジェットキャップに達した場合は <a href="https://www.visacashapprb.com/en/" target="_blank">Visa CashApp</a> の利用をご検討ください。</li>
    </ul>
    <p>※Bun-payのご利用は計画的に。</p>
</div>
"""
st.markdown(legal_notice_html, unsafe_allow_html=True)


dazn_image = 'dazn-logo-8.png'

# 中央揃えのためのカラムを作成
col1, col2, col3,col4,col5= st.columns([1,1,1,1,1])

# 中央のカラムにロゴを配置
with col3:

    # バナー画像を表示
    st.image(dazn_image)

# アプリの最後にフッターを追加
footer_html = """
<style>
.footer {
    position: fixed;
    right: 0;
    bottom: 0;
    left: 0;
    text-align: center;
    margin-right: 20px;
    font-size: smaller;
}
</style>
<div class="footer">
    &copy; powered by DAZN EXTREME ENGINEERING 2024
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
