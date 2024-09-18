import '../styles/CardStyles.css'

type CardProps = {
  title: string;
  points: number;
  comments: number;
}

const Card = ({title, points, comments} : CardProps) => {
  return (
    <div className='card-container'> 
      <h3>{title}</h3>
      <div className='card-content'>
        <div className='card-category'>
          <p>Points</p>
          <span>{points}</span>
        </div>
        <div className='card-category'>
          <p>Comments</p>
          <span>{comments}</span>
        </div>
      </div>
    </div>
  )
}

export default Card
