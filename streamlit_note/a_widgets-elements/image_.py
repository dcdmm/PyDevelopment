import streamlit as st

st.image(
    # nochrome image of shape (w,h) or (w,h,1) OR a color image of shape (w,h,3) OR an RGBA image of shape (w,h,4) OR a URL to fetch the image from OR a path of a local image file OR an SVG XML string like <svg xmlns=...</svg> OR a list of one of the above, to display multiple images.
    image="image_e0.png",
    # mage caption. If displaying multiple images, caption should be a list of captions (one for each image).
    caption="可爱的猫猫"
)

st.image(
    image="http://sucimg.itc.cn/sblog/o4178e48bcb2ff67de98496c3a437fcee",
    caption="美食"
)