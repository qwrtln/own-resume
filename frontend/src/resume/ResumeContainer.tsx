import React from "react";
import Resume from "./Resume";
import { ResumeModel } from "./ResumeModel";

const ResumeContainer = () => (
  <div>
    <Resume {...getResumeFromRedux()} />
  </div>
);

function getResumeFromRedux(): ResumeModel {
  return {
    basics: {
      name: "Анджей Вьонцек",
      summary: "Pro Gram I Sta",
      email: "Proprietary (not Gmail for sure)",
    },
    work: [
      {
        company: "Szel",
        position: "Go Developer",
        summary:
          "Andrzeju, tańcz i pij, " +
          "A z Szela sobie kpij, " +
          "A z Szela kpij sobie, kpij!",
      },
      {
        company: "Akamaj",
        position: "Super Señor Developer",
        summary: "Sprawiam, że Netflix działa",
      },
    ],
  };
}

export default ResumeContainer;
