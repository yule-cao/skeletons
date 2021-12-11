import { Person } from "../main/model";

test("Create new Person", () => {
  expect(new Person("YU").toString()).toBe("YU");
});
