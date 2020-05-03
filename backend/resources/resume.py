from typing import Tuple

from flask_restful import Resource

resume_json = '''{
    basics: {
      name: "Andrew Вьонцек",
      summary: "Pro Gram I Sta",
      email: "Proprietary (not Gmail for sure)",
    },
    work: [
      {
        company: "Szel",
        position: "Go Developer",
        summary:
          "Andrzeju, tańcz i pij, A z Szela sobie kpij, A z Szela kpij sobie, kpij!",
      },
      {
        company: "Akamaj",
        position: "Super Señor Developer",
        summary: "Sprawiam, że Netflix działa",
      },
    ]
  }'''


class Resume(Resource):
    def get(self) -> Tuple[str, int]:
        return resume_json.replace("\n", ""), 200
