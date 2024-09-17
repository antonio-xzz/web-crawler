interface DetailErrorResponse {
    loc: string[];
    msg: string;
    type: string;
}
interface StatusMessageFunction<T> {
    (error: T): string;
}

type StatusMessage = string | StatusMessageFunction<any>;
interface StatusMessages {
    [statusCode: number | string]: StatusMessage;
}

export const statusMessages: StatusMessages = {
    422: (error: { response: { data: { detail: DetailErrorResponse[] } } }) => {
        const details = error.response.data.detail;
        const message = details
            .map(
                (detail: DetailErrorResponse) =>
                    `${detail.loc.join("-")}: ${detail.msg}`
            )
            .join(", ");
        return message;
    },
    409: (error: { response: { data: { message: string } } }) =>
        error.response.data.message,
};
