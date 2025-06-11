import streamlit as st
import qrcode
from qrcode.constants import ERROR_CORRECT_M #誤り訂正レベル
from PIL import Image #画像処理
import io #Web上で画像ファイルを管理する

st.set_page_config(page_title="QRコード生成アプリ", page_icon="black")

st.title("QRコード生成")
st.write("テキストやURLを入力するとQRコードが生成されます。")

# 入力フォーム
input_text = st.text_input("QRコードにしたいURLを入力してください")

# QRコード生成ボタン
if st.button("QRコードを生成"):
    if input_text.strip() == "":
        st.warning("URLを入力してください")
    else:
        # QRコード生成
        qr = qrcode.QRCode(
            #QRコードのサイズ
            version = 1,
            #誤り訂正レベル
            error_correction=ERROR_CORRECT_M,
            #ボックスサイズ
            box_size = 10,
            #幅
            border=4
        )
        qr.add_data(input_text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        #ダウンロードリンク作成
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        #QRコード表示
        st.image(byte_im, caption="生成されたQRコード", use_column_width=False)

        #ダウンロードボタン
        st.download_button(
            label="保存",
            data=byte_im,
            file_name="qr_code.png",
            mime="image/png"
        )