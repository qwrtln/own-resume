import React from "react";
import { render } from "@testing-library/react";
import Resume from "./Resume";

test("render resume with workplaces section", () => {
  const { getByText } = render(
    <Resume
      basics={{ name: "Johnny Python", email: "" }}
      work={[
        {
          company: "Company 1",
        },
      ]}
    />
  );

  const linkElement = getByText(/Workplaces:/i);
  expect(linkElement).toBeInTheDocument();
});
