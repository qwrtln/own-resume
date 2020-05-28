import React from "react";
import { render } from "@testing-library/react";
import Resume from "./Resume";

test("render resume", () => {
   let resume = render(
    <Resume
      basics={{ name: "Johnny Python", email: "" }}
      work={[
        {
          company: "Company 1",
        },
      ]}
    />
  );

  expect(resume).toMatchSnapshot();
});
