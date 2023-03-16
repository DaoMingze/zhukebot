from ..config import config
from .base import DrawBase

class Draw(DrawBase):
    """队列中的单个请求"""
    MAX_RESOLUTION: int = 32

    async def fromresp(self, resp):
        img: dict = await resp.json()
        return img["images"][0]

    async def run(self):
        site = config.sd_site
        header = {
            "content-type": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        }
        post_api = (
            f"http://{site}/sdapi/v1/img2img"
            if self.img2img
            else f"http://{site}/sdapi/v1/txt2img"
        )
        for i in range(self.batch):
            parameters = {
                "prompt": self.tags,
                "seed": self.seed[i],
                "steps": self.steps,
                "cfg_scale": self.scale,
                "width": self.width,
                "height": self.height,
                "negative_prompt": self.ntags,
                "sampler": self.sampler,
                "CLIP_stop_at_last_layers": self.clip,
                "override_settings": {
                    "CLIP_stop_at_last_layers": 2,
                    "sd_model_checkpoint": self.model,
                },
            }
            if self.img2img:
                parameters.update(
                    {
                        "init_images": ["data:image/jpeg;base64," + self.image],
                        "denoising_strength": self.strength,
                    }
                )
            await self.post_(header, post_api, parameters)
