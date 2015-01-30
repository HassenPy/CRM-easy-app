from pipeline.compressors import CompressorBase
from csscompressor import compress


class CSSCompressor(CompressorBase):

    def compress_css(self, css):
        return compress(css)
