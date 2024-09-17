export class GeneralErrorResponse {
    message: string;
    status_code: number;
  
    constructor(message: string, status_code: number) {
      this.message = message;
      this.status_code = status_code;
    }
  }
