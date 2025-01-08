# -*- coding: utf-8 -*-
from aip import AipOcr
import io
from process.logger import logger

class OCR:

    def __init__(self, appId, apiKey, secretKey):
        self.client = AipOcr(appId, apiKey, secretKey)

    def _pil2bin(self, pilObj):
        bin = io.BytesIO()
        pilObj.save(bin, format='PNG')
        return bin.getvalue()

    def _ocr(self, img):
        imgBin = self._pil2bin(img)
        return self.client.basicGeneral(imgBin)

    def run(self, quesImg, answImg):
        ques = self._ocr(quesImg)
        answ = self._ocr(answImg)

        ques = ''.join([item['words'] for item in ques['words_result']])
        answ = [item['words'] for item in answ['words_result']]

        return ques, answ
