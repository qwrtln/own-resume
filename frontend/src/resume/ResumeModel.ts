export interface ResumeModel {
  basics: BasicsModel;
  work: WorkModel[];
}

export interface BasicsModel {
  name: String;
  label?: String;
  picture?: String;
  email: String;
  phone?: String;
  website?: String;
  summary?: String;
}

export interface WorkModel {
  company: String;
  position?: String;
  website?: String;
  startDate?: String;
  endDate?: String;
  summary?: String;
}
