# -*- coding: utf-8 -*-
import base64
import io
import logging

from odoo import models

_logger = logging.getLogger(__name__)


class ResCompany(models.Model):
    _inherit = "res.company"

    def get_mw_print_logo(self):
        """Return company logo with empty top/side padding cropped for printouts."""
        self.ensure_one()
        if not self.logo:
            return False
        try:
            from PIL import Image

            raw = base64.b64decode(self.logo)
            image = Image.open(io.BytesIO(raw)).convert("RGBA")
            width, height = image.size
            pixels = image.load()

            def is_content(x, y):
                r, g, b, a = pixels[x, y]
                if a < 16:
                    return False
                # Treat near-white as empty padding in the logo canvas
                return not (r > 245 and g > 245 and b > 245)

            top = next((y for y in range(height) if any(is_content(x, y) for x in range(width))), 0)
            bottom = next(
                (y for y in range(height - 1, -1, -1) if any(is_content(x, y) for x in range(width))),
                height - 1,
            )
            left = next((x for x in range(width) if any(is_content(x, y) for y in range(height))), 0)
            right = next(
                (x for x in range(width - 1, -1, -1) if any(is_content(x, y) for y in range(height))),
                width - 1,
            )

            # Keep a little side/bottom padding; no top padding so the mark sits flush
            pad = max(2, int(min(width, height) * 0.02))
            box = (
                max(0, left - pad),
                max(0, top),
                min(width, right + 1 + pad),
                min(height, bottom + 1 + pad),
            )
            cropped = image.crop(box)

            buf = io.BytesIO()
            cropped.save(buf, format="PNG")
            return base64.b64encode(buf.getvalue())
        except Exception:
            _logger.exception("Failed to crop Midwestern print logo for company %s", self.id)
            return self.logo
