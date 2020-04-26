export interface ResumeModel {
  basics: BasicsModel;
  work: WorkModel[];
}

export interface BasicsModel {
  name: string;
  label?: string;
  picture?: string;
  email: string;
  phone?: string;
  website?: string;
  summary?: string;
}

export interface WorkModel {
  company: string;
  position?: string;
  website?: string;
  startDate?: string;
  endDate?: string;
  summary?: string;
}
